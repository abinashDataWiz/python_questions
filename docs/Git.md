This is all the commands you need to know for Git


### Clone a Repo
```bash
git clone (URL For repo)
```
This gets a local copy of the repo on your machine. It will automatically create a folder from your current directory with the same name as the repo name on GitHub.


### Pull changes
```bash
git pull
```

This gets the latest changes that were commited to your branch. Note if you hace local changes in the same files that are changed you get merge conflicts. 


### Pushing your code using commands 

Stage all the changes you want in Git

```bash
git add .
```

Make a commit followed by a message 

```bash
git commit -m "feat: added UI" 
```

Push your code now
```bash
git push
```


### Dealing with Merge Conflicts 

If you have local changes when you git pulled, stash them then pull again 

```bash
git stash
git pull
git pop
```
Then you have to figure out the merge conflict by accepting incoming or your changes or both. 


