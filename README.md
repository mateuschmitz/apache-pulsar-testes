# Apache Pulsar Cluster

Este repositório é uma PoC do Pulsar, permitindo a execução de um cluster localmente.

## Requisitos


- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

## Executando

Altere a memória utilizada pelo futuro cluster:

```bash
$ minikube config set memory 8192
```

Crie um cluster com o minikube

```bash
$ minikube start
```

Após a criação do cluster, inicie a criação dos pods. Os primeiros pods a serem criados são os do Zookeeper:

```bash
$ kubectl apply -f 01-zookeeper.yml
```

Aguarde até que os pods estejam rodando, isso pode levar alguns minutos. Para verificar quais pods estão rodando execute:

```bash
$ kubectl get pods
```

Em seguida execute os demais arquivos, na ordem abaixo:

- `02-cluster-metadata.yml`
- `03-bookie.yml`
- `04-broker.yml`
- `05-admin.yml`
- `06-monitoring.yml`
- `07-proxy.yml`

## Utilizando

Com todos os pods operacionais, é possível utilizar as interfaces disponíveis. Para acesso, será utilizado o IP do cluster, criado pelo minikube. Para checar o IP execute:

```bash
$ minikube ip
```

As seguintes interfaces estarão disponíveis:

- Pusar Broker `<ip_cluster>:30001`
- Pusar Broker `<ip_cluster>:30002`
- Prometheus `<ip_cluster>:30003`
- Grafana `<ip_cluster>:30004`
- Pulsar Dashboard `<ip_cluster>:30005`

## Instalando Pulsar Client

```bash
$ pip install pulsar-client
```

## Produzindo mensagens

Altere o IP do cluster no arquivo [producer.py](producer.py) e execute:

```bash
$ python producer.py
```

## Consumindo mensagens

Altere o IP do cluster no arquivo [consumer.py](consumer.py) e execute:

```bash
$ python consumer.py
```

