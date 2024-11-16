import subprocess
import webbrowser


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
        return True
    except subprocess.CalledProcessError as e:
        print("Error saat menjalankan 'git push':", e)
        return False


def get_repository_url():
    """Mendapatkan URL repository GitHub dari konfigurasi git"""
    try:
        # Mendapatkan URL dari remote origin
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            check=True,
            stdout=subprocess.PIPE,
            text=True,
        )
        remote_url = result.stdout.strip()

        # Menyesuaikan URL agar langsung ke halaman repository GitHub
        if remote_url.startswith("git@github.com:"):
            # SSH URL: git@github.com:username/repository.git
            remote_url = remote_url.replace("git@github.com:", "https://github.com/")
        elif remote_url.startswith("https://"):
            # HTTPS URL: https://github.com/username/repository.git
            remote_url = remote_url

        # Menghapus akhiran '.git' jika ada
        if remote_url.endswith(".git"):
            remote_url = remote_url[:-4]

        return remote_url
    except subprocess.CalledProcessError as e:
        print("Error saat mendapatkan URL repository:", e)
        return None


def open_browser(url):
    """Membuka browser untuk melihat hasil perubahan"""
    try:
        webbrowser.open(url, new=2)  # new=2 membuka tab baru jika memungkinkan
        print(f"Browser dibuka di: {url}")
    except Exception as e:
        print("Error saat membuka browser:", e)


if __name__ == "__main__":
    # Meminta pesan commit dari user
    commit_message = input("Masukkan pesan commit: ")

    # Menjalankan perintah Git
    git_add()
    git_commit(commit_message)

    if git_push():
        # Mendapatkan URL repository
        repository_url = get_repository_url()
        if repository_url:
            open_browser(repository_url)