from tofupy import Tofu
from pathlib import Path


def plan_terraform(
    terraform_dir: str,
    terraform_vars: dict[str, str] | None = None,
    backend_path: str | None = None,
    extra_args: list[str] | None = None,
    plan_path: Path | None = None,
):
    print("Planning terraform..")
    workspace = Tofu(
        cwd=(terraform_dir),
        binary="terraform",
    )

    print("Running terraform init..")
    if backend_path:
        workspace.init(backend_conf=backend_path)
    else:
        workspace.init()

    print("Running terraform plan..")
    plan_log, plan_results = workspace.plan(
        variables=terraform_vars or {},
        extra_args=extra_args or [],
        plan_file=plan_path,
    )

    if plan_log.errors:
        print("Terraform plan failed!")
        for diagnostic in plan_log.errors:
            print(f"Error: {diagnostic.summary}")
    else:
        print("Terraform plan complete..")
        print(
            f"Added: {getattr(plan_log, 'added', 0)}, Changed: {getattr(plan_log, 'changed', 0)}, Removed: {getattr(plan_log, 'removed', 0)}"
        )

    return plan_log, plan_results
