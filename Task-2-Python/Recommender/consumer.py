import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()


from places.models import Place
params = pika.URLParameters('amqps://jdtjagnk:Ih1YgdWzGAm5oT5wOndktYAa4gEhkBqh@puffin.rmq2.cloudamqp.com/jdtjagnk')

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print("Received in admin")
    data = json.loads(body)
    print(data)

    if properties.content_type == "place_yes":
        place = Place.objects.get(id = id)
        place.yes+=1
        place.save()
    
    elif properties.content_type == "place_no":
        place = Place.objects.get(id = id)
        place.no+=1
        place.save() 

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack = True)
print("Started Consuming")
channel.start_consuming()
channel.close()
