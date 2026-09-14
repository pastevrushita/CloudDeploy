import subprocess

print("Starting deployment...")

subprocess.run(["docker", "build", "-t", "clouddeploy", "."], check=True)

subprocess.run(
    ["docker", "run", "-d", "-p", "5000:5000", "--name", "clouddeploy-app", "clouddeploy"],
    check=True
)

print("Deployment completed successfully!")