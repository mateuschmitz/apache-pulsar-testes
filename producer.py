import pulsar

client = pulsar.Client('pulsar://<ip_cluster>:30002')
producer = client.create_producer('test-topic')

for i in range(100000):
    producer.send(('hello-pulsar-%d' % i).encode('utf-8'))
    print("Sending message: '%s'" % i)

client.close()
