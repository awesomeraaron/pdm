# Design Doc
https://docs.google.com/document/d/16hHb8ljCYuKtjnBn6B94uBC72it3rvjprWJ4joCBA3s/edit?usp=sharing

# Note
The project is still in progress and has not yet reached completion. The existing code serves as an initial demonstration, illustrating the approach outlined in the design document.

# How to use
step 1
```
source ./bin/activate
```

step 2
```
python ./app.py
```

step 3
open your local host
```
http://127.0.0.1:5000
```

## query you could try:

```python
# get all fitments
"""
{
  allFitments(sort: [YEAR_ASC]){
    edges {
      node{
        id,
        year,
        maker,
        model,
      }
    }
  }
}
"""

# get all parts
"""
{
  allParts{
    edges {
      node{
        id,
        fitment {
          maker,
          year,
          model,
        },
        sku {
          name,
          price,
          description,
          skuId,
          image {
            imageUri
          },
        }
        metaData,
      }
    }
  }
}
"""


# create an image, then query it
"""
mutation {
  mutateImage(imageUri:"www.google.com"){
    image {
      id
    }
  }
}
"""
# note: it will return empty since the mutation happen in a separate sessions. Ideally, there will be a standalone session management module.
# When do a new query like the following, we can see the image is added to DB indeed.
"""
query {
  allImages {
    edges {
      node {
        id,
        imageUri
      }
    }
  }
}
"""
```