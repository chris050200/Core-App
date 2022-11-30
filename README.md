# Voltage Sample Data

Sample API to get voltage data
<br>
{"time":"22:18:09.712613","voltage":1688}
<br><br>
Open a terminal<br>
$ git clone https://github.com/chris050200/Core-App.git <br>
$ pip install flask<br>
$ pip install -U flask-cors<br>
$ python voltageAPI.py<br>

then go to : http://127.0.0.1:5005/voltage and you should see a voltage sample<br>
{"time":"22:18:09.712613","voltage":1688}<br>

or : http://127.0.0.1:5005/voltage2 for an array <br>

{"data":[{"time":"22:18:40.028784","voltage":1681},{"time":"22:18:40.028784","voltage":1687},{"time":"22:18:40.028784","voltage":1662},{"time":"22:18:40.028784","voltage":1682},{"time":"22:18:40.028784","voltage":1657},{"time":"22:18:40.028784","voltage":1669},{"time":"22:18:40.028784","voltage":1665},{"time":"22:18:40.028784","voltage":1665},{"time":"22:18:40.028784","voltage":1693},{"time":"22:18:40.028784","voltage":1683},{"time":"22:18:40.028784","voltage":1666},{"time":"22:18:40.028784","voltage":1658},{"time":"22:18:40.028784","voltage":1692}...<br>
