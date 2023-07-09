#!/bin/bash
GREEN="\e[32m"
ENDCOLOR="\e[0m"

python3.9 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
python3 blogicum/manage.py migrate
python3 blogicum/manage.py loaddata db.json
python3 blogicum/manage.py createsuperuser

echo -e "
${GREEN}****************************\nУстановка проекта завершена.\n****************************${ENDCOLOR}
\nСервер можно запустить сейчас или позднее выполнив команду ${GREEN}python3 manage.py runserver${ENDCOLOR}
в папке проекта ${GREEN}./django_blog/blogicum/${ENDCOLOR}"

answer="N"
while true; do
  read -p "Выполнить запуск сервера [Y/N]: " answer
  case "$answer" in
  n | N | y | Y) break ;;
  esac
done

if [[ "$answer" = [yY] ]]; then
  python3 blogicum/manage.py runserver
fi
