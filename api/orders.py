class Parcel:
    """class that describes the parcel object"""
    def __init__(self, order_id, user_id, email, status,
                 item_to_be_shipped, weight,
                 name_of_sender, name_of_reciever,
                 destination, item_origin):
        """constructor to intialise the parameters
        of the Parcel class
        """

        self.order_id = order_id
        self.user_id = user_id
        self.email = email
        self.status = status
        self.item_to_be_shipped = item_to_be_shipped
        self.weight = weight
        self.name_of_sender = name_of_sender
        self.name_of_reciever = name_of_reciever
        self.destination = destination
        self.item_origin = item_origin
