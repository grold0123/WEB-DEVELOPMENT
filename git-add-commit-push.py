 
import subprocess

# Stage all files
subprocess.run(["git", "add", "."])

# Commit
subprocess.run(["git", "commit", "-m", "Update project"])

# Push
subprocess.run(["git", "push"])
