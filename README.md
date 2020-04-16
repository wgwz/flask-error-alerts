# Flask Error Alerts with Twilio Sendgrid

Full tutorial can be found here: 

This code shows how to send an email alert every time an unhandled exception occurs.

## Getting Started

### Installing

```
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

### Config

Create a `.env` file in project directory with the following:

```
SENDGRID_API_KEY=yourkey
FROM_EMAIL=youremail
TO_EMAIL=youremail
```

### Running locally

```
(venv) $ flask run
```

Visit [localhost:5000/](localhost:5000/)

## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [Twilio Sendgrid](https://www.twilio.com/sendgrid) - Email Service 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
