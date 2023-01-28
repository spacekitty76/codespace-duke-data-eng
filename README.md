Python for devops codespace repo

# Development Set Up
## Set up codespaces
- Open my [repo](https://github.com/spacekitty76/)
    - Fork it in your GitHub account
- Open [Codespaces](https://github.com/codespaces)
    - Choose "new codespace"
    - Choose the repo you just created when forking mine above

## Installing dependencies locally
- Create and activate a virtual environment
    - ```python3 -m venv venv```
    - ```source /venv/bin/activate```
- Install dependencies
    - ```make install``` will intall everything you need

# Watching the build on GitHub servers
- This repo has a GitHub Actions workflow
- It uses GitHubs build servers to run everything in the Makefile on the GitHub servers
    - So basically... the `make install` you did locally also happens on GitHubs build servers when you push code
- Go to your repo (your fork of my repo)
    - Click on 'actions'
    - Click on your latest build to view the progress
