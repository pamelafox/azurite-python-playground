# Azurite Dev Container / Codespace

This repository includes a <a target="_blank" href="https://containers.dev/">dev container definition</a> for use with <a target="_blank" href="https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers">VS Code Dev Containers</a> extension or <a target="_blank" href="https://github.com/features/codespaces">GitHub Codespaces</a>.

Inside the <code>.devcontainer</code> folder, the <code>devcontainer.json</code> uses the <code>docker-compose.yaml</code> to set up a local <a target="_blank" href="https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azurite?tabs=docker-hub%2Cblob-storage">Azurite server</a> inside the container and sets the <code>AZURE_STORAGE_CONNECTION_STRING</code> environment variable to point to it.

You can then use the Python script <code>main.py</code> along with the azure-storage-blob Python SDK to interact with the Azurite server.