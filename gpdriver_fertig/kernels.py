import tempfile
import shutil
import requests
import tarfile
import subprocess
import urllib.request

def unpackTarfile(fname, path):
    if (fname.endswith("tar.gz")):
        tar = tarfile.open(fname, "r:gz")
        tar.extractall(path=path)
        tar.close()
    elif (fname.endswith("tar")):
        tar = tarfile.open(fname, "r:")
        tar.extractall(path=path)
        tar.close()

def updateKernels():
    with tempfile.TemporaryDirectory() as tmpdirname:
        fname = tmpdirname + '/release.tar.gz'
        r = requests.get('https://api.github.com/repos/FertigLab/CondaEnvironments/releases/latest')
        url = r.json()['assets'][0]['browser_download_url']
        urllib.request.urlretrieve(url, fname)
        unpackTarfile(fname, tmpdirname)
        install_dir = tmpdirname + '/FertigCondaEnvironments/'
        subprocess.call(install_dir + 'install.sh', cwd=install_dir)

