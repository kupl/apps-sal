def services(service_list):
    hdpt = 'Homie dont play that!'
    names = [req.split()[2].capitalize() + '! ' + hdpt for req in service_list]
    return names


def nkotb_vs_homie(requirements):
    monitoring = services(requirements[0])
    automation = services(requirements[1])
    deployment = services(requirements[2])
    cloud = services(requirements[3])
    microservices = services(requirements[4])
    report = '{} monitoring objections, {} automation, {} deployment pipeline, {} cloud, and {} microservices.'.format(len(monitoring), len(automation), len(deployment), len(cloud), len(microservices))
    compiled = []
    compiled += monitoring
    compiled += automation
    compiled += deployment
    compiled += cloud
    compiled += microservices
    compiled.append(report)
    print(compiled)
    return compiled
