FROM python:latest
# update packages
RUN apt update -y && apt upgrade -y
# add packages
RUN apt install git
# Install BUN
RUN curl -fsSL https://bun.sh/install | bash && \
  ln -s $HOME/.bun/bin/bun /usr/local/bin/bun

# Chart generator phase
WORKDIR /chart-generator
RUN git clone https://github.com/Reda2200/workout-chart.git ./
COPY workouts.csv .
RUN pip install --root-user-action=ignore  -r requirements.txt
RUN python3 main.py

# web server
WORKDIR /app
RUN git clone https://github.com/AREA44/astro-multiverse.git ./
RUN rm -rf /app/src/assets/*
RUN cp /chart-generator/graph/* /app/src/assets/
RUN bun install
RUN bun astro preferences disable devToolbar

# Container command
CMD ["bun", "start", "--host"]