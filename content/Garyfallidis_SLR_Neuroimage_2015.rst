:title: The Streamline-based Linear Registration (SLR) paper is now available in Neuroimage
:date: 2015-06-15 20:20
:category: blog

I am very pleased to inform you that the paper 

Garyfallidis et al., "**Robust and efficient linear registration of white-matter fascicles in the space of streamlines**", Neuroimage 2015, is now available online `here <http://www.sciencedirect.com/science/article/pii/S1053811915003961>`_.

This link below allows for free access of the paper for a couple of weeks 

http://authors.elsevier.com/a/1R8x23lc~qsfWv

The main idea is depicted in the figure below. If you have a bundle, as a set of streamlines, you can directly register it with SLR to homologous bundles. The results are
very robust to incomplete data which are omnipotent in tractography.

.. raw:: html

	<p align="center">
	<a href="http://www.sciencedirect.com/science/article/pii/S1053811915003961">
	<img src="images/all_to_one_4_new.png" alt="alt text" title="Streamline-based Linear Registration (SLR)" width="500px" align="center" />
	</a>
	</p>


The SLR is a killer application for the world of diffusion MRI as it allows you to:

1. Register incomplete bundles of the same type from different subjects.
2. Create sharp bundle-specific atlases.
3. Register left to right bundles directly for lateralization experiments.
4. Perform efficient whole brain linear registration.

The method is already available in DIPY and I have a simple tutorial here
http://dipy.org/examples_built/bundle_registration.html#example-bundle-registration

The next days I will upload new more advanced tutorials and show you how to
generate the results of the paper with your datasets.

Happy hacking!
