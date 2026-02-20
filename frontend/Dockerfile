FROM node:18 AS build

WORKDIR /app

# only package files first
COPY package*.json ./

# install dependencies
RUN npm install

# now copy source code
COPY . .

# build project
RUN npm run build

# production server
FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80
