#!/bin/python3


Google_certs_draft = {
    "Date": "Course name --Google",
    "052223": "Networking 101",
    "051823": "Deploying a fault-tolerant MS active directory environment",
    "062523": "Architecting w/ Google Kubernetes Engine --Specialization",
    "050623": "Networking in Google cloud: Defining & Implementing Networks",
}

for ke, va in Google_certs_draft.items():
    print("{}\t| {}".format(ke, va))

print("------------------------------\n")

Amazon_certs_draft = {
    "Date": "Course name --Amazon",
    "070123": "AWS Fundamentals: Addressing Security Risk",

}

for ki, vi in Amazon_certs_draft.items():
    print("{}\t| {}".format(ki, vi))

print("------------------------------\n")

MS_certs_draft = {
    "Date": "Course name --Microsoft",
    "051823": "Secure your Cloud Data",
    "042923": "Microsoft Azure management tools & Security solutions",
}

for kv, vv in MS_certs_draft.items():
    print("{}\t| {}".format(kv, vv))

print("------------------------------\n")

