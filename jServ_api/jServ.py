import requests


class jServ:
    def __init__(self, url, port, key):
        self.url = url
        self.port = port
        self.key = key

    # ----------------------------GET Requests----------------------------

    # Queries a collection for a specific object by id. Returns the whole object in JSON
    def send_query(self, db, id):
        q = {"db": db, "id": id}
        h = {"x-api-key": self.key}
        return requests.get(
            "http://{0}:{1}/query".format(self.url, self.port), params=q, headers=h
        ).json()

    # Queries a collection for a specific attribute of an object by id and name
    # Returns the attribute value in an AttributeContainer object
    def send_query_attribute(self, db, id, a):
        q = {"db": db, "id": id, "a": a}
        h = {"x-api-key": self.key}
        return requests.get(
            "http://{0}:{1}/query/attribute".format(self.url, self.port),
            params=q,
            headers=h,
        ).json()

    # Queries a collection for all attributes of a specific key in every object
    # If an object does not have an attribute of the passed key, the object is skipped
    # The query returns a list of all the attributes keyed by object id.
    def send_query_allAttributes(self, db, a):
        q = {"db": db, "a": a}
        h = {"x-api-key": self.key}
        return requests.get(
            "http://{0}:{1}/query/allAttributes".format(self.url, self.port),
            params=q,
            headers=h,
        ).json()

    # Queries a collection for objects that share the same value of a specific attribute
    # If an object does not have an attribute of the passed key, the object is skipped
    # The query returns a list of all the objects with the attribute and value
    # (Requires an AttributeContainer JSON object to be passed in the body)
    def send_query_byAttributes(self, db, a, attribute):
        q = {"db": db, "a": a}
        h = {"x-api-key": self.key}
        return requests.get(
            "http://{0}:{1}/query/byAttributes".format(self.url, self.port),
            params=q,
            headers=h,
            data=attribute,
        ).json()

    # Returns an unused id in a collection
    def send_query_newId(self, db):
        q = {"db": db}
        h = {"x-api-key": self.key}
        return requests.get(
            "http://{0}:{1}/query/byAttributes".format(self.url, self.port),
            params=q,
            headers=h,
        ).json()

    # ----------------------------POST Requests----------------------------

    # Adds a new empty object to a collection by id
    def send_add(self, db, id):
        q = {"db": db, "id": id}
        h = {"x-api-key": self.key}
        return requests.post(
            "http://{0}:{1}/add".format(self.url, self.port), params=q, headers=h
        ).json()

    # Adds a new JSON object to a collection
    # (Requires an DataObject JSON object to be passed in the body)
    def send_add_object(self, db, obj):
        q = {"db": db}
        h = {"x-api-key": self.key}
        return requests.post(
            "http://{0}:{1}/add/object".format(self.url, self.port),
            params=q,
            headers=h,
            data=obj,
        ).json()

    # Adds an attribute to an object in a collection by id
    # (Requires an AttributeContainer JSON object to be passed in the body)
    def send_add_attribute(self, db, id, a, obj):
        q = {"db": db, "id": id, "a": a}
        h = {"x-api-key": self.key}
        return requests.post(
            "http://{0}:{1}/add/attribute".format(self.url, self.port),
            params=q,
            headers=h,
            data=obj,
        ).json()

    # Modifies the id of an object in a collection by id
    def send_mod_object(self, db, id, v):
        q = {"db": db, "id": id, "v": v}
        h = {"x-api-key": self.key}
        return requests.post(
            "http://{0}:{1}/mod/object".format(self.url, self.port),
            params=q,
            headers=h,
        ).json()

    # Modifies an attribute of an object in a collection by id
    # (Requires an AttributeContainer JSON object to be passed in the body)
    def send_mod_attribute(self, db, id, a, attribute):
        q = {"db": db, "id": id, "a": a}
        h = {"x-api-key": self.key}
        return requests.post(
            "http://{0}:{1}/mod/attribute".format(self.url, self.port),
            params=q,
            headers=h,
            data=attribute,
        ).json()

    # ----------------------------DELETE Requests----------------------------

    # Deletes an object from a collection by id
    def send_delete_object(self, db, id):
        q = {"db": db, "id": id}
        h = {"x-api-key": self.key}
        return requests.post(
            "http://{0}:{1}/delete/object".format(self.url, self.port),
            params=q,
            headers=h,
        ).json()

    # Deletes an attribute from an object by id
    def send_delete_attribute(self, db, id, a):
        q = {"db": db, "id": id, "a": a}
        h = {"x-api-key": self.key}
        return requests.post(
            "http://{0}:{1}/delete/attribute".format(self.url, self.port),
            params=q,
            headers=h,
        ).json()
