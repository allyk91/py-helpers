from pathlib import Path

from tofupy import Tofu


def init_terraform(
    terraform_dir: str,
    backend_path: Path | None = None,
    disable_backends: bool = False,
    extra_args: list[str] | None = None,
):
    print("Initializing terraform..")
    workspace = Tofu(
        cwd=(terraform_dir),
        binary="terraform",
    )

    print("Running terraform init..")
    init_ok = workspace.init(
        disable_backends=disable_backends,
        backend_conf=backend_path,
        extra_args=extra_args or [],
    )

    if init_ok:
        print("Terraform init complete..")
    else:
        print("Terraform init failed!")

    return init_ok
