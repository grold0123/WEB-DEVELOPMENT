 
import subprocess

# Stage all files
subprocess.run(["git", "add", "."], check=True)

# Commit
subprocess.run(["git", "commit", "-m", "Update project"])

# Push
subprocess.run(["git", "push"], check=True)
