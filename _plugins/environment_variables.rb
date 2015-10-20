module Jekyll

  class EnvironmentVariablesGenerator < Generator

    def generate(site)
      site.config['env'] = ENV['JEKYLL_ENV'] || 'github'
      # Add other environment variables to `site.config` here...
      if  (site.config['env'] == 'github')
        site.config['deploy']="https://guzmanhe.github.io" 
      else 
        site.config['deploy']="http://alt.qcri.org/~guzmanhe/"
      end
    end

  end

end
