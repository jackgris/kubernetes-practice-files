from os import path

import yaml

from kubernetes import client, config

def main():
    config.load_kube_config()
    
    with open(path.join(path.dirname(__file__),
                        'nginx-deployment.yaml')) as f:
        dep = yaml.safe_load(f)
        k8s = client.AppsV1Api()
        dep = k8s.create_namespaced_deployment(body=dep,
                                               namespace="default")
        print(f"Deployment created. status='{dep.status}'")
            
if __name__ == '__main__':
    main()
