# github-action-test
Test github actions with python. 
- main.yml -> Send an email automatically on push. 

# Instructions Setting up GitHub Actions

Follow these steps to create a new repository on GitHub, add a GitHub Actions workflow, and print a message on each push.

## Step 1: Create a new repository on GitHub

1. Go to [GitHub](https://github.com/) and log in to your account.
2. Click on the "New" button to create a new repository.
3. Fill in the repository information, such as name, description, and other details according to your preferences.
4. Check the option "Initialize this repository with a README" if you want to add a README.md file to the repository.
5. Click on "Create repository" to create the repository.

## Step 2: Create an action file

1. Inside your new repository, click on the "Actions" tab at the top.
2. Select "Set up a workflow yourself" to start with a custom action file.

## Step 3: Edit the action file

Replace the content of the `.github/workflows/main.yml` file with the following example:

```yaml
name: My First Workflow

on: [push]

jobs:
  print-message:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Print message
      run: echo "Hello from my GitHub Action!" 
```

## Step 4: Create an action file
1. Save the changes in the .github/workflows/main.yml file.
2. Commit the changes with a descriptive message like "Add GitHub Actions workflow."
3. Push the changes to your repository.

## Step 5: Check the action status
1. Go to the "Actions" tab in your GitHub repository.
2. You should see your new workflow either in progress or completed. Click on it to view details and execution logs.




