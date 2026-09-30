FROM node:25

WORKDIR /app/web

COPY package.json /app/web

RUN npm i 

COPY . /app/web

CMD ["npm", "run", "dev", "--", "--host"]