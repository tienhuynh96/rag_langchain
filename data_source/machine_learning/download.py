import os
import gdown

id = "1IbnAT_hfQBMYw0nlqS67NVT9RIr7UaXs"
gdown.download(id=id, quiet=False)

os.system("unzip -o ml_docs.zip")
os.system("rm ml_docs.zip")
