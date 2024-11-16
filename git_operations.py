import subprocess

def git_add():
    """Menjalankan perintah 'git add .'"""
    try:
        subprocess.run(["git", "add", "."], check=True)
        print("Semua perubahan telah ditambahkan.")
    except subprocess.CalledProcessError as e:
        print("Error saat menjalankan 'git add .':", e)

def git_commit(message):
    """Menjalankan perintah 'git commit -am' dengan pesan yang diberikan"""
    try:
        subprocess.run(["git", "commit", "-am", message], check=True)
        print(f"Perubahan berhasil di-commit dengan pesan: {message}")
    except subprocess.CalledProcessError as e:
        print("Error saat menjalankan 'git commit':", e)

def git_push():
    """Menjalankan perintah 'git push origin main'"""
    try:
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("Perubahan berhasil di-push ke branch 'main'.")
    except subprocess.CalledProcessError as e:
        print("Error saat menjalankan 'git push':", e)

if __name__ == "__main__":
    # Meminta pesan commit dari user
    commit_message = input("Masukkan pesan commit: ")

    # Menjalankan perintah Git
    git_add()
    git_commit(commit_message)
    git_push()