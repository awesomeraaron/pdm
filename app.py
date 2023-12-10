#!/usr/bin/env python

from database import db_session, init_db
from flask import Flask
from schema import schema

from flask_graphql import GraphQLView

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    "/", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    init_db()
    app.run()




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