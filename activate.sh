# Shortcut for activating any venv found in the current dir. Run using `source activate.sh`

source $(find . | grep -E "^./v?env.*/bin/activate$")
