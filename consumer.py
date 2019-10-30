import pulsar

client = pulsar.Client('pulsar://<ip_cluster>:30002')
consumer = client.subscribe('test-topic', subscription_name='consumer01')

while True:
    msg = consumer.receive()
    print("Received message: '%s'" % msg.data())
    consumer.acknowledge(msg)

client.close()
