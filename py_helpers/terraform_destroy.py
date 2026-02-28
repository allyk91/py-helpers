from tofupy import Tofu
from pathlib import Path


def destroy_terraform(
    terraform_dir: str,
    terraform_vars: dict[str, str] | None = None,
    backend_path: str | None = None,
    extra_args: list[str] | None = None,
):
    print("Destroying terraform..")
    workspace = Tofu(
        cwd=(terraform_dir),
        binary="terraform",
    )

    print("Running terraform init..")
    if backend_path:
        workspace.init(backend_conf=backend_path)
    else:
        workspace.init()

    print("Running terraform destroy..")
    destroy_results = workspace.apply(
        variables=terraform_vars or {},
        destroy=True,
        extra_args=extra_args or [],
    )

    if destroy_results.errors:
        print("Terraform destroy failed!")
        for diagnostic in destroy_results.errors:
            print(f"Error: {diagnostic.summary}")
    else:
        print("Terraform destroy complete..")
        print(
            f"Added: {destroy_results.added}, Changed: {destroy_results.changed}, Removed: {destroy_results.removed}"
        )

    return destroy_results
