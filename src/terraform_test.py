from tofupy import Tofu
import os

def test_terraform(terraform_dir: str):
    print("Testing terraform..")
    workspace = Tofu(
        cwd=(terraform_dir),
        binary="terraform",
    )
    
    print("Running terraform format..")
    fmt = workspace._run(args=["fmt"])
    print(f"{fmt}")

    workspace.init(disable_backends=True)

    # Validate configuration
    validation = workspace.validate()
    if not validation.valid:
        print("Configuration is invalid!")
        for diagnostic in validation.diagnostics:
            print(f"Error: {diagnostic.summary}")
    else:
        print("Terraform is valid..")

if __name__ == "__main__":
    print("no directo")