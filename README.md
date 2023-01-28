Python for devops codespace repo

# Development Set Up
- Open my [repo](https://github.com/spacekitty76/)
    - Fork it in your GitHub account
- Open [Codespaces](https://github.com/codespaces)
    - Choose "new codespace"
    - Choose the repo you just created when forking mine above

## Installing dependencies locally
- ```make install``` will intall everything you need

# Watching the build
- This repo has a GitHub Actions workflow
- It uses GitHubs build servers to run everything in the Makefile on the GitHub servers
    - So basically... the `make install` you did locally also happens on GitHubs build servers when you push code
- Go to your repo (your fork of my repo)
    - Click on 'actions'
    - Click on your latest build to view the progress
