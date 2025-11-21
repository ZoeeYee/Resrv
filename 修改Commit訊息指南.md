# 📝 修改 Commit 訊息指南

## 🎯 你的情況

目前只有 **1 個 commit**，最簡單的方法是直接修改它。

---

## 方法 1：修改最後一個 Commit（推薦）

### 步驟：

```powershell
# 1. 修改最後一個 commit 訊息
git commit --amend -m "Initial commit: Integrate Firebase Auth and Secured API"

# 2. 強制推送到 GitHub（因為修改了歷史）
git push --force-with-lease
```

**注意：** `--force-with-lease` 比 `--force` 更安全，會檢查遠端是否有其他人的提交。

---

## 方法 2：修改多個 Commit（如果有多個）

如果之後有多個 commit 需要修改，使用互動式 rebase：

```powershell
# 1. 開始互動式 rebase（修改最近 3 個 commit）
git rebase -i HEAD~3

# 2. 會打開編輯器，將要修改的 commit 前面的 "pick" 改為 "reword" 或 "r"
# 例如：
# pick abc1234 舊訊息 1
# reword def5678 舊訊息 2  ← 改成 reword
# pick ghi9012 舊訊息 3

# 3. 儲存並關閉編輯器
# 4. Git 會逐個打開編輯器讓你修改每個 commit 訊息
# 5. 完成後強制推送
git push --force-with-lease
```

---

## 方法 3：批量修改所有 Commit 訊息

如果要修改所有 commit 訊息，使用 filter-branch：

```powershell
# 修改所有 commit 訊息中的特定文字
git filter-branch -f --msg-filter 'sed "s/舊文字/新文字/g"' HEAD

# 或使用更複雜的替換
git filter-branch -f --msg-filter '
  if [ "$GIT_COMMIT" = "07378813384a75d14a42b5e9e23dd1b815e97fff" ]; then
    echo "Initial commit: Integrate Firebase Auth and Secured API"
  else
    cat
  fi
' HEAD

# 完成後強制推送
git push --force-with-lease
```

---

## ⚠️ 重要提醒

### Force Push 的風險

1. **會覆蓋遠端歷史**：如果其他人已經 clone 了你的倉庫，他們的歷史會不一致
2. **只適合個人專案**：如果是個人專案，沒問題
3. **使用 `--force-with-lease`**：比 `--force` 更安全

### 何時可以使用

- ✅ 個人專案
- ✅ 只有你一個人在使用
- ✅ 還沒有人 clone 你的倉庫
- ✅ 想要清理 commit 歷史

### 何時不應該使用

- ❌ 多人協作的專案
- ❌ 已經有人 clone 了你的倉庫
- ❌ 公開的開源專案（除非是新的專案）

---

## 🚀 快速執行（你的情況）

因為你只有 1 個 commit，執行以下命令：

```powershell
# 修改 commit 訊息為英文（避免編碼問題）
git commit --amend -m "Initial commit: Integrate Firebase Auth and Secured API"

# 推送到 GitHub
git push --force-with-lease
```

---

## 📋 Commit 訊息最佳實踐

### 好的 Commit 訊息格式：

```
類型: 簡短描述

詳細說明（可選）
```

### 類型範例：

- `feat:` - 新功能
- `fix:` - 修復 bug
- `docs:` - 文件更新
- `style:` - 程式碼格式（不影響功能）
- `refactor:` - 重構
- `test:` - 測試
- `chore:` - 其他（建置、工具等）

### 範例：

```
feat: Add Firebase authentication
fix: Resolve login token issue
docs: Update README with setup instructions
refactor: Improve API error handling
```

---

## ✅ 完成後檢查

修改完成後：

1. 檢查本地 commit：
   ```powershell
   git log --oneline
   ```

2. 檢查 GitHub：
   訪問 https://github.com/ZoeeYee/Resrv/commits/main

---

## 🎯 總結

對於你的情況（只有 1 個 commit），最簡單的方法是：

```powershell
git commit --amend -m "Initial commit: Integrate Firebase Auth and Secured API"
git push --force-with-lease
```

這樣就能把 commit 訊息改成英文，避免編碼問題！

