import pika, json
from main import Place, db
params = pika.URLParameters('amqps://jdtjagnk:Ih1YgdWzGAm5oT5wOndktYAa4gEhkBqh@puffin.rmq2.cloudamqp.com/jdtjagnk')

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print("Received in main")
    data = json.loads(body)
    print(data)

    if properties.content_type == "place_created":
        place = Place(id = data["id"], title=data["title"], image=data["image"])
        db.session.add(place)
        db.session.commit()
        print("Place Created")

    elif properties.content_type == "place_updated":
        place = Place.query.get(data['id'])
        place.title = data["title"]
        place.image = data["image"]
        db.session.commit()
        print("Place Updated")

    elif properties.content_type == "place_deleted":
        place = Place.query.get(data)
        db.session.delete(place)
        db.session.commit()
        print("Place Deleted")


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack = True)
print("Started Consuming")
channel.start_consuming()
channel.close()
