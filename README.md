# Things near my bus stop API

## Purpose

We built this application during a weekend hackathon event called #build4stl hosted by OpenDataSTL. This API serves as an HTTP accessible service that, given a bus stop coordinate pair returns a type of venue within r (default=500 meters) from the Foursquare API.

There is no reason that this couldn't include more than just STL Metro GTFS data but right now that is an assumption that is hardcoded.

## API Documentation

`GET /routes/<route_id>`
Takes a parameter called `query` that essentially is the type of venue you are looking for.

## Deployment to Heroku

This app should be easily deployed to Heroku. The only consideration is that you'll need to an environment variable called `FOURSQUARE_KEY`

You can use `heroku config:set FOURSQUARE_KEY=YOURKEYGOESHEREBUTMAKESURETONEVERCOMMITIT`
