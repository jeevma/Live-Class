To **fork a GitHub repo**, **keep it updated**, and **push your own changes**, follow this step-by-step guide. This setup allows you to:

* Regularly **pull changes from the original repository** (called `upstream`)
* Make your own **changes in your fork**
* **Push your changes** to *your own* GitHub fork

---

## ✅ Step-by-Step Setup

---

### **1. Fork the Original Repo**

* Go to the original GitHub repository (e.g., `https://github.com/someuser/project`)
* Click the **Fork** button (top right)
* This creates a **copy in your GitHub account**, e.g., `https://github.com/yourusername/project`

---

### **2. Clone Your Fork Locally**

```bash
git clone https://github.com/yourusername/project.git
cd project
```

---

### **3. Add the Original Repo as Upstream**

```bash
git remote add upstream https://github.com/someuser/project.git
```

* Now, your repo has two remotes:

  * `origin` → your GitHub fork
  * `upstream` → original repo

Check remotes:

```bash
git remote -v
```

---

### **4. Pull Updates from the Original Repo**

Whenever you want to sync with the original repo:

```bash
# Fetch all branches from upstream
git fetch upstream

# Merge changes from upstream/main into your local main
git checkout main
git merge upstream/main
```

If the original repo uses `master` instead of `main`, adjust accordingly.

---

### **5. Push Updates to Your Fork**

After merging upstream changes:

```bash
git push origin main
```

---

### **6. Make Your Own Changes**

* Create a feature branch (recommended):

```bash
git checkout -b feature/my-change
```

* Make your changes
* Stage and commit:

```bash
git add .
git commit -m "My changes"
```

* Push to your GitHub:

```bash
git push origin feature/my-change
```

---

### **7. Merge Back to Main (Optional)**

Once you're ready to merge your changes:

```bash
git checkout main
git merge feature/my-change
git push origin main
```

---

### **8. Keep Pulling and Repeating**

* Regularly pull from `upstream`
* Rebase/merge as needed
* Push your updated `main` or branches to your fork

---

## 🔁 Summary Command Cheat Sheet

| Action                         | Command                                                        |
| ------------------------------ | -------------------------------------------------------------- |
| Fork and clone                 | `git clone https://github.com/yourname/repo.git`               |
| Add upstream                   | `git remote add upstream https://github.com/original/repo.git` |
| Fetch upstream changes         | `git fetch upstream`                                           |
| Merge upstream into local main | `git merge upstream/main`                                      |
| Push to your GitHub            | `git push origin main`                                         |
| Create new feature branch      | `git checkout -b feature/name`                                 |
| Push feature branch            | `git push origin feature/name`                                 |

---

Would you like a bash script or a `Makefile` to automate any of these steps?
