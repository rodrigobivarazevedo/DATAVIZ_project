# The App

### JSON Rest API

The app provides raw json data or FHIR data via the routes:

- /patientID/raw/
- /patientID/fhir/
- /Blood_tests/raw/patientID
- /Blood_tests/fhir/patientID

### The HTML views

- / (Heatmap View from a specific blood test of a Patient)
- red = outside normal range
- yellow = close to outside range
- green = normal range
  
![Alt Text](heatmap3.png)
