# Quick Setup for PyPI Publishing (Trusted Publishing)

## What You Need to Do

### 1. Push to GitHub
```bash
cd /Users/t0thkr1s/Downloads/gpp-decrypt
git add .
git commit -m "Modernize project for PyPI publishing"
git push origin main
```

### 2. Configure PyPI Trusted Publishing
1. Go to https://pypi.org and create an account (if you don't have one)
2. Go to your project: https://pypi.org/manage/project/gpp-decrypt/settings/publishing/
3. Add a new trusted publisher:
   - **Owner**: `t0thkr1s`
   - **Repository name**: `gpp-decrypt`
   - **Workflow name**: `publish.yml`
   - **Environment name**: (leave blank)
4. Click "Add"

### 3. Trigger Publishing

#### Option A: Create a Release Tag
```bash
git tag v2.0.0
git push origin v2.0.0
```

#### Option B: Manual Trigger
1. Go to https://github.com/t0thkr1s/gpp-decrypt/actions
2. Click "Publish to PyPI" workflow
3. Click "Run workflow"
4. Select master branch and run

## That's it!

No API tokens needed! GitHub will authenticate directly with PyPI.
Your package will be live at: https://pypi.org/project/gpp-decrypt/
