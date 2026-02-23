provider "aws" {
  region = "ap-south-1"
}

resource "aws_security_group" "realestate_sg" {
  name        = "realestate-sg"
  description = "Allow SSH and HTTP"

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "App"
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "realestate_server" {
  ami           = "ami-0f5ee92e2d63afc18"
  instance_type = "t3.micro"
  key_name      = "realestate"

  vpc_security_group_ids = [aws_security_group.realestate_sg.id]

  tags = {
    Name = "RealEstate-IaC"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt update -y",
      "sudo apt install docker.io -y",
      "sudo systemctl start docker",
      "sudo systemctl enable docker",

      "sudo apt install git -y",
      "git clone https://github.com/vidhi4104/real-estate-fullstack.git",
      "cd real-estate-fullstack",

      "sudo docker compose up -d"
    ]

    connection {
      type        = "ssh"
      user        = "ubuntu"
      private_key = file("realestate.pem")
      host        = self.public_ip
    }
  }
}
