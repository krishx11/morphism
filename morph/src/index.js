import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Github, Linkedin, Mail } from "lucide-react"
import Link from "next/link"

export default function Home() {
  return (
    <div className="min-h-screen bg-background text-foreground">
      {/* Hero Section */}
      <section className="py-20 px-4 text-center">
        <h1 className="text-4xl font-bold mb-4">AI Morph detection Model</h1>
        <p className="text-xl mb-8 max-w-2xl mx-auto">
          Explore our cutting-edge AI model for image analysis and classification.
        </p>
        <Button size="lg" asChild>
          <a href="#model">Explore Model</a>
        </Button>
      </section>

      {/* About Section */}
      <section className="py-16 px-4 bg-muted">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold mb-6">About the Project</h2>
          <p className="text-lg mb-4">
            Our project leverages state-of-the-art Convolutional Neural Networks (CNNs) to analyze and classify images with
            high accuracy. We've also incorporated GAN detection technology to identify artificially generated images.
          </p>
          <p className="text-lg">
            This showcase demonstrates the power and potential of AI in image processing and analysis, pushing the boundaries
            of what's possible in computer vision.
          </p>
        </div>
      </section>

      {/* Model Interaction Section */}
      <section id="model" className="py-16 px-4">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold mb-6">Interact with the Model</h2>
          <Card>
            <CardHeader>
              <CardTitle>Upload an Image</CardTitle>
            </CardHeader>
            <CardContent>
              <Input type="file" accept="image/*" className="mb-4" />
              <Button>Analyze Image</Button>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* Output Display Section */}
      <section className="py-16 px-4 bg-muted">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold mb-6">Model Output</h2>
          <Card>
            <CardHeader>
              <CardTitle>Analysis Results</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-lg mb-4">
                The model has analyzed your image. Here are the results:
              </p>
              <ul className="list-disc list-inside space-y-2">
                <li>Classification: Natural Landscape</li>
                <li>Confidence: 95.7%</li>
                <li>GAN Detection: Not artificially generated (99.9% confidence)</li>
              </ul>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* Contact Section */}
      <footer className="py-8 px-4 bg-background">
        <div className="max-w-4xl mx-auto flex justify-center space-x-6">
          <Link href="https://github.com" className="text-foreground hover:text-primary">
            <Github className="h-6 w-6" />
            <span className="sr-only">GitHub</span>
          </Link>
          <Link href="mailto:contact@example.com" className="text-foreground hover:text-primary">
            <Mail className="h-6 w-6" />
            <span className="sr-only">Email</span>
          </Link>
          <Link href="https://linkedin.com" className="text-foreground hover:text-primary">
            <Linkedin className="h-6 w-6" />
            <span className="sr-only">LinkedIn</span>
          </Link>
        </div>
      </footer>
    </div>
  )
}
