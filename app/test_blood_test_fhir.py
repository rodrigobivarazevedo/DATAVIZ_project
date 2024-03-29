import requests
import json

# test /process_cmp endpoint
cmp_fhir = {
    "resourceType": "Bundle",
    "type": "collection",
    "entry": [
        
      {
        "fullUrl": "urn:uuid:4d3b31e4-9a4b-4c03-80e9-1d633f261e20",
        "resource": {
          "resourceType": "Observation",
          "status": "final",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "1742-6",
                "display": "Alanine aminotransferase [Enzymatic activity/volume] in Serum or Plasma"
              }
            ],
            "text": "Alanine aminotransferase [Enzymatic activity/volume] in Serum or Plasma"
          },
          "valueQuantity": {
            "value": 30,
            "unit": "U/L"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:5db7d90d-6c7b-4e2f-ba22-5e4e47d6862a",
        "resource": {
          "resourceType": "Observation",
          "status": "final",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "1751-7",
                "display": "Albumin [Mass/volume] in Serum or Plasma"
              }
            ],
            "text": "Albumin [Mass/volume] in Serum or Plasma"
          },
          "valueQuantity": {
            "value": 4.2,
            "unit": "g/dL"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:0b978f4f-bbd3-4a06-baae-9837baf89673",
        "resource": {
          "resourceType": "Observation",
          "status": "final",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "6768-6",
                "display": "Alkaline phosphatase [Enzymatic activity/volume] in Serum or Plasma"
              }
            ],
            "text": "Alkaline phosphatase [Enzymatic activity/volume] in Serum or Plasma"
          },
          "valueQuantity": {
            "value": 75,
            "unit": "U/L"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:3b7b70f2-062f-47aa-8b3a-c7db1206a1f7",
        "resource": {
          "resourceType": "Observation",
          "status": "final",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "88112-8",
                "display": "Asp"
              }
            ],
            "text": "Asp"
          },
          "valueQuantity": {
            "value": 25,
            "unit": "U/L"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:2d5f919c-2a6e-41b5-bafe-695575a01c6d",
        "resource": {
          "resourceType": "Observation",
          "status": "final",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "1963-8",
                "display": "Bicarbonate [Moles/volume] in Serum or Plasma"
              }
            ],
            "text": "Bicarbonate [Moles/volume] in Serum or Plasma"
          },
          "valueQuantity": {
            "value": 24,
            "unit": "mmol/L"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:015d7ac5-3085-421b-befd-dfb30d77b789",
        "resource": {
          "resourceType": "Observation",
          "status": "final",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "6299-2",
                "display": "Urea nitrogen [Mass/volume] in Blood"
              }
            ],
            "text": "Urea nitrogen [Mass/volume] in Blood"
          },
          "valueQuantity": {
            "value": 15,
            "unit": "mg/dL"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:7f12e5a9-61b1-40c1-8a56-76fbd0ff5ab5",
        "resource": {
          "resourceType": "Observation",
          "status": "final",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "2075-0",
                "display": "Chloride [Moles/volume] in Serum or Plasma"
              }
            ],
            "text": "Chloride [Moles/volume] in Serum or Plasma"
          },
          "valueQuantity": {
            "value": 102,
            "unit": "mmol/L"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:5407a599-e3d1-4f86-a43a-ff3c0724db1d",
        "resource": {
          "resourceType": "Observation",
          "status": "final",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "2093-3",
                "display": "Cholesterol [Mass/volume] in Serum or Plasma"
              }
            ],
            "text": "Cholesterol [Mass/volume] in Serum or Plasma"
          },
          "valueQuantity": {
            "value": 180,
            "unit": "mg/dL"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:cd62e585-461d-4ed2-8f4a-794a57a70fb2",
        "resource": {
          "resourceType": "Observation",
          "status": "final",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "2157-6",
                "display": "Creatine kinase [Enzymatic activity/volume] in Serum or Plasma"
              }
            ],
            "text": "Creatine kinase [Enzymatic activity/volume] in Serum or Plasma"
          },
          "valueQuantity": {
            "value": 100,
            "unit": "U/L"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:876a1b58-05a0-4f8b-bfe6-cc4d4d7e47c1",
        "resource": {
          "resourceType": "Observation",
          "status": "final",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "38483-4",
                "display": "Creatinine [Mass/volume] in Blood"
              }
            ],
            "text": "Creatinine [Mass/volume] in Blood"
          },
          "valueQuantity": {
            "value": 0.9,
            "unit": "mg/dL"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:7112d4f5-c736-4f23-9b9a-066a94ef4e8e",
        "resource": {
          "resourceType": "Observation",
          "status": "final",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "2324-2",
                "display": "Gamma glutamyl transferase [Enzymatic activity/volume] in Serum or Plasma"
              }
            ],
            "text": "Gamma glutamyl transferase [Enzymatic activity/volume] in Serum or Plasma"
          },
          "valueQuantity": {
            "value": 40,
            "unit": "U/L"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:1cbf1992-0d54-4a2e-83d7-3f3f787bd8b1",
        "resource": {
          "resourceType": "Observation",
          "status": "final",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "2336-6",
                "display": "Globulin [Mass/volume] in Serum"
              }
            ],
            "text": "Globulin [Mass/volume] in Serum"
          },
          "valueQuantity": {
            "value": 2.5,
            "unit": "g/dL"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:2adfb0c1-2e2b-43bf-93f0-10375c15f56d",
        "resource": {
          "resourceType": "Observation",
          "status": "final",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "2339-0",
                "display": "Glucose [Mass/volume] in Blood"
              }
            ],
            "text": "Glucose [Mass/volume] in Blood"
          },
          "valueQuantity": {
            "value": 110,
            "unit": "mg/dL"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:4b4a1dbf-d9e2-4d42-8f23-684a32ee612f",
        "resource": {
          "resourceType": "Observation",
          "status": "preliminary",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "2498-4",
                "display": "Iron [Mass/volume] in Serum or Plasma"
              }
            ],
            "text": "Iron [Mass/volume] in Serum or Plasma"
          },
          "valueQuantity": {
            "value": 90,
            "unit": "µg/dL"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:0ccce248-4414-4f0a-a58b-8cb7d9d1a30c",
        "resource": {
          "resourceType": "Observation",
          "status": "final",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "2532-0",
                "display": "Lactate dehydrogenase [Enzymatic activity/volume] in Serum or Plasma"
              }
            ],
            "text": "Lactate dehydrogenase [Enzymatic activity/volume] in Serum or Plasma"
          },
          "valueQuantity": {
            "value": 200,
            "unit": "U/L"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:43e99406-041e-43e2-98f7-c076d1eb8353",
        "resource": {
          "resourceType": "Observation",
          "status": "preliminary",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "2692-2",
                "display": "Osmolality of Serum or Plasma"
              }
            ],
            "text": "Osmolality of Serum or Plasma"
          },
          "valueQuantity": {
            "value": 290,
            "unit": "mmol/kg"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:dda9e13f-0f76-4b12-82ea-54f206f68d17",
        "resource": {
          "resourceType": "Observation",
          "status": "final",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "2777-1",
                "display": "Phosphate [Mass/volume] in Serum or Plasma"
              }
            ],
            "text": "Phosphate [Mass/volume] in Serum or Plasma"
          },
          "valueQuantity": {
            "value": 3.5,
            "unit": "mg/dL"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:63a85e48-59cc-49b2-95c4-6f1302094f0d",
        "resource": {
          "resourceType": "Observation",
          "status": "final",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "6298-4",
                "display": "Potassium [Moles/volume] in Blood"
              }
            ],
            "text": "Potassium [Moles/volume] in Blood"
          },
          "valueQuantity": {
            "value": 4.0,
            "unit": "mmol/L"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:31cc5d8a-2b7a-4a91-9f68-e3bdc90c4f7e",
        "resource": {
          "resourceType": "Observation",
          "status": "final",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "2947-0",
                "display": "Sodium [Moles/volume] in Blood"
              }
            ],
            "text": "Sodium [Moles/volume] in Blood"
          },
          "valueQuantity": {
            "value": 138,
            "unit": "mmol/L"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:4c79e4fc-229f-4b20-bb35-8c4a2842518b",
        "resource": {
          "resourceType": "Observation",
          "status": "final",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "42719-5",
                "display": "Bilirubin.total [Mass/volume] in Blood"
              }
            ],
            "text": "Bilirubin.total [Mass/volume] in Blood"
          },
          "valueQuantity": {
            "value": 1.0,
            "unit": "mg/dL"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:1f6ef2a1-4f5b-4b6f-bb87-d792f1c7a25a",
        "resource": {
          "resourceType": "Observation",
          "status": "preliminary",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "17861-6",
                "display": "Calcium [Mass/volume] in Serum or Plasma"
              }
            ],
            "text": "Calcium [Mass/volume] in Serum or Plasma"
          },
          "valueQuantity": {
            "value": 9.5,
            "unit": "mg/dL"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:97e3b9d4-77f4-4f88-b645-5834e19f227a",
        "resource": {
          "resourceType": "Observation",
          "status": "final",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "2885-2",
                "display": "Protein [Mass/volume] in Serum or Plasma"
              }
            ],
            "text": "Protein [Mass/volume] in Serum or Plasma"
          },
          "valueQuantity": {
            "value": 7.0,
            "unit": "g/dL"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:1f83e14d-e2c8-40f5-85b3-937843e3bb8c",
        "resource": {
          "resourceType": "Observation",
          "status": "final",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "14927-8",
                "display": "Triglyceride [Moles/volume] in Serum or Plasma"
              }
            ],
            "text": "Triglyceride [Moles/volume] in Serum or Plasma"
          },
          "valueQuantity": {
            "value": 150,
            "unit": "mg/dL"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      },
      {
        "fullUrl": "urn:uuid:75739a3a-9813-407f-a251-84277f5cd4d5",
        "resource": {
          "resourceType": "Observation",
          "status": "final",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "3084-1",
                "display": "Urate [Mass/volume] in Serum or Plasma"
              }
            ],
            "text": "Urate [Mass/volume] in Serum or Plasma"
          },
          "valueQuantity": {
            "value": 6.0,
            "unit": "mg/dL"
          },
          "effectiveDateTime": "2022-01-04T08:00:00Z"
        }
      }
    ]
  }
  


# Flask endpoint URL
url = "http://127.0.0.1:5000/process_cmp"

# Make a POST request with JSON payload
response = requests.post(url, json=cmp_fhir)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Request was successful!")
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)  # Print the response content for debugging