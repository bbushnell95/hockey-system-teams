from invoke import task

IMAGE_NAME_DEFAULT = "bbushnell95/hockey-system-teams"
IMAGE_TAG_DEFAULT = "latest"

@task
def build(c, image_name="", image_tag=""):
    """
    Method to build the docker application.
    """
    full_image_path = get_final_image_params(image_name, image_tag)
    c.run("docker build -t {image_name}:{image_tag} .".format(**full_image_path))


@task
def push(c, image_name="", image_tag=""):
    """
    Method to push the docker image to dockerhub.
    """
    full_image_path = get_final_image_params(image_name, image_tag)
    c.run("docker push {image_name}:{image_tag}".format(**full_image_path))


@task
def start(c, image_name="", image_tag=""):
    """
    Method to start the docker container.
    """
    full_image_path = get_final_image_params(image_name, image_tag)
    c.run("IMAGE_NAME={image_name} IMAGE_TAG={image_tag} docker-compose up".format(**full_image_path))


@task
def startdev(c, image_name="", image_tag=""):
    """
    Method to start the docker container in dev mode.
    """
    full_image_path = get_final_image_params(image_name, image_tag)
    c.run("IMAGE_NAME={image_name} IMAGE_TAG={image_tag} docker-compose -f docker-compose.dev.yml up".format(**full_image_path))


def get_final_image_params(image_name, image_tag):
    """
    Helper function to help with getting the final image name and tag.
    """
    return {
        "image_name": image_name or IMAGE_NAME_DEFAULT,
        "image_tag": image_tag or IMAGE_TAG_DEFAULT
    }