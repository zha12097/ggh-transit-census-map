# Uploading this clean repository using the GitHub website

1. Download and extract the accompanying ZIP file on your computer.
2. If you are replacing a previous repository that exposed source data, first confirm you have a backup and understand that deleting a GitHub repository does not recall previously copied data. Delete the old repository from **Settings → General → Danger Zone → Delete this repository**.
3. Create a **new Public repository with the identical name** `ggh-transit-census-map`. Do not initialize it with a README or a `.gitignore`.
4. In the empty repository choose **uploading an existing file**. Drag *everything inside* the extracted folder into the uploader—not the ZIP or the top-level containing folder. Ensure dotfiles `.nojekyll`, `.gitignore`, and the `.github` directory are included. If necessary, upload these separately.
5. Confirm `index.html` and `README.md` will be at repository root. Commit to `main` with a message such as `Publish cleaned GGH map and documentation`.
6. In **Settings → Pages** choose **Deploy from a branch**, `main`, `/(root)`, and save.
7. Open https://zha12097.github.io/ggh-transit-census-map/ and check all map controls. Wait for deployment to finish and hard-refresh if the earlier version remains cached.
8. Open **Actions → Check map** and verify the workflow completes successfully.

The ZIP contains no separate source datasets. The public `index.html` embeds geographic features and Census figures required to display the map; visitors can inspect or extract them. No public static HTML file can make those displayed values confidential.

See `docs/MAINTENANCE.md` for details and test commands.
