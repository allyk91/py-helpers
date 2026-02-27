from tofupy import Tofu


def apply_terraform(terraform_dir: str, terraform_vars: dict[str, str] | None = None):
    print("Deploying terraform..")
    workspace = Tofu(
        cwd=(terraform_dir),
        binary="terraform",
    )

    print("Running terraform init..")
    workspace.init()

    print("Running terraform apply..")
    apply_results = workspace.apply(variables=terraform_vars or {})

    if apply_results.errors:
        print("Terraform apply failed!")
        for diagnostic in apply_results.errors:
            print(f"Error: {diagnostic.summary}")
    else:
        print("Terraform apply complete..")
        print(
            f"Added: {apply_results.added}, Changed: {apply_results.changed}, Removed: {apply_results.removed}"
        )

    return apply_results
