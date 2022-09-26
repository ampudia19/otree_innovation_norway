@echo off
echo # Settings env vars #
cmd /c "set OTREE_ADMIN_PASSWORD=in_experiment"
cmd /c "set OTREE_PRODUCTION=1"
cmd /c "set OTREE_AUTH_LEVEL=STUDY"

echo # Running prodserver #
cmd /c "cd %IN_IGL% & cd .38/Scripts/ & call activate.bat & cd ../.."
cmd /c "otree runprodserver 10.60.133.110:80"
