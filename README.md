
                          Basic Bots

  What is it?
  -----------

  The basic bots allows a client to connect to a variable number of bots, 
  run witha docker-compose --scale. All services dockerized and ready to use
  with docker-compose.

  Documentation
  -------------

  Included in the doc directory.

  Dependencies
  ------------

  All included in the docker base image lserraga/base_image:

      * Flask: for creating the REST server endpoints.
      * Requests: for the HTTP requests.
      * Chatterbot: for creating the bots.

  Files
  --------

  /doc/
      usage.txt : Documentation of the design usage.

  /src/
      /Client/
          Dockerfile: contains the commands to build the client container.
          main.py: source code for the client app.
      /bot/
          Dockerfile: contains the commands to build the bot container.
          main.py: source code for the bot.

  docker-compose.yml : contains the commands to build and run all the containers.
  bot-cli.py: source code to run the app in CLI mode.
  bot-slack.py: source code to run the app connected to slack.

  Contacts
  --------

  Luis Serra Garcia, Creator: luikserra@gmail.com
