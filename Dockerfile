FROM python:latest
RUN apt update -y && apt upgrade -y
RUN apt install git nginx -y
WORKDIR /var/www/html
COPY workouts.csv .
RUN rm *.html
RUN git clone https://github.com/Reda2200/workout-chart.git ./
RUN pip install --root-user-action=ignore  -r requirements.txt
RUN python3 ./main.py

CMD ["nginx", "-g", "daemon off;"]