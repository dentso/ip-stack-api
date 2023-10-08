# README

Retrieves the longitude and latitude for a given ip address using IPStack API


## Pre-requisites
- Signup and obtain an api key from [IPStack](https://ipstack.com/)
- Clone this repo
- Build and run (next step)


## Build and run
```bash
export API_KEY="***"
docker build . -t python-ipaddr:0.0.1
docker run --rm -it -e API_KEY=$API_KEY python-ipaddr:0.0.1 134.201.250.155
{
  "latt": 34.0655517578125,
  "long": -118.24053955078125
}

```

