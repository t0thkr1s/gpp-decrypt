# Quick Setup for PyPI Publishing

## What You Need to Do

### 1. Push to GitHub
```bash
cd /Users/t0thkr1s/Downloads/gpp-decrypt
git add .
git commit -m "Modernize project for PyPI publishing"
git push origin main
```

### 2. Get PyPI Token
1. Go to https://pypi.org and create an account (if you don't have one)
2. Go to Account Settings → API tokens
3. Click "Add API token"
4. Name: "gpp-decrypt"
5. Scope: "Entire account" (or project-specific after first upload)
6. Copy the token (starts with `pypi-`)

### 3. Add Token to GitHub
1. Go to your repo: https://github.com/t0thkr1s/gpp-decrypt
2. Click Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Name: `PYPI_API_TOKEN`
5. Value: Paste your PyPI token
6. Click "Add secret"

### 4. Create a Release
```bash
# Create and push a tag
git tag v2.0.0
git push origin v2.0.0
```

This will automatically:
- Build your package
- Upload it to PyPI
- Make it installable via `pip install gpp-decrypt`

## That's it!

Your package will be live on PyPI in a few minutes.
Check it at: https://pypi.org/project/gpp-decrypt/
