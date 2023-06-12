"""
pip install selenium bs4 requests
"""
import datetime
import logging
import os
import sys

import requests

logger = logging.getLogger("myip")
# {"ip":"x.x.x.x","country":"Italy","cc":"IT"}
MYIPCOM = "https://api.myip.com/"
# only html page
WHATISMYIPADDRESS = "https://whatismyipaddress.com/"

WHATSMYIP = "https://api.whatismyip.com/ip.php?key="
API_KEY = ""


def myip(log_level=logging.INFO):
    """
    Get your public ip using different services
    :param log_level: logging level
    :return: None
    """
    logger.setLevel(log_level)
    handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(handler)

    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    logger.debug("START at %s", utc_timestamp)
    ip_list = []

    resp_myip = make_request(url=MYIPCOM)
    if resp_myip.ok:
        logger.debug("MYIPCOM: OK")
        logger.debug(resp_myip.text)
        diz = resp_myip.json()
        ip_list.append(diz.get("ip"))
    else:
        logger.exception("MYIPCOM: KO")
        raise Exception("Call KO. Error! MYIPCOM: {}".format(MYIPCOM))

    resp_whatismyip = make_request(url=WHATSMYIP)
    if resp_whatismyip.ok:
        logger.debug("WHATSMYIP: OK")
        logger.debug(resp_whatismyip.text)
        ip_list.append(resp_whatismyip.text)
    else:
        logger.exception("WHATSMYIP: KO")
        raise Exception("Call KO. Error! WHATSMYIP: {}".format(WHATSMYIP))

    resp_whatismyipaddress = get_ip_from_html(url=WHATISMYIPADDRESS)
    if resp_whatismyipaddress:
        logger.debug("WHATISMYIPADDRESS: OK")
        logger.debug(resp_whatismyipaddress)
        ip_list.append(resp_whatismyipaddress)
    else:
        logger.exception("WHATISMYIPADDRESS: KO")
        raise Exception("Call KO. Error! WHATISMYIPADDRESS: {}".format(WHATISMYIPADDRESS))

    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    logger.info(f"IP LIST: {ip_list}")
    logger.debug("END at %s", utc_timestamp)


def make_request(url):
    """
    Make a request to the url
    :param url:
    :return: response
    """
    logger.debug("MAKING A REQUEST to url: {}".format(url))
    response = requests.get(url)
    logger.debug("Response Status Code: {}, Status: {}".format(response.status_code, response.ok))

    return response


def get_ip_from_html_page(url):
    """
    Get the ip from the html page
    :param url:
    :return: ip
    """
    from bs4 import BeautifulSoup
    from selenium import webdriver

    # Crea un'istanza del driver del browser.
    # In questo esempio, stiamo utilizzando Firefox, ma potresti anche utilizzare Chrome o altri.
    # Assicurati di avere il driver appropriato installato e disponibile nel tuo PATH.
    driver = webdriver.Chrome()
    ip = None
    try:
        # Visita la pagina web.
        driver.get(url)

        # Lascia che il JavaScript venga eseguito.
        # Il tempo di attesa dipenderà dal tuo caso specifico.
        driver.implicitly_wait(10)

        # Ottieni il codice sorgente HTML della pagina.
        html = driver.page_source

        # Analizza il codice HTML con BeautifulSoup.
        soup = BeautifulSoup(html, 'html.parser')

        # Trova il tag desiderato.
        p_tag = soup.find(id='ipv4')

        # Stampa il testo del tag.
        ip = p_tag.text
    except Exception as e:
        logger.exception("Exception: {}".format(e))
    finally:
        # Chiudi il driver del browser.
        driver.quit()
    return ip


myip()
