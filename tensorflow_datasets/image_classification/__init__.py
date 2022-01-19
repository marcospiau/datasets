# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Image Classification datasets."""

from tensorflow_datasets.image_classification.beans import Beans
from tensorflow_datasets.image_classification.bee_dataset import BeeDataset
from tensorflow_datasets.image_classification.bigearthnet import Bigearthnet
from tensorflow_datasets.image_classification.binary_alpha_digits import BinaryAlphaDigits
from tensorflow_datasets.image_classification.caltech import Caltech101
from tensorflow_datasets.image_classification.caltech_birds import CaltechBirds2010
from tensorflow_datasets.image_classification.cars196 import Cars196
from tensorflow_datasets.image_classification.cassava import Cassava
from tensorflow_datasets.image_classification.cats_vs_dogs import CatsVsDogs
from tensorflow_datasets.image_classification.cbis_ddsm import CuratedBreastImagingDDSM
from tensorflow_datasets.image_classification.chexpert import Chexpert
from tensorflow_datasets.image_classification.cifar import Cifar10
from tensorflow_datasets.image_classification.cifar import Cifar100
from tensorflow_datasets.image_classification.cifar10_1 import Cifar10_1
from tensorflow_datasets.image_classification.cifar10_corrupted import Cifar10Corrupted
from tensorflow_datasets.image_classification.citrus import CitrusLeaves
from tensorflow_datasets.image_classification.cmaterdb import Cmaterdb
from tensorflow_datasets.image_classification.colorectal_histology import ColorectalHistology
from tensorflow_datasets.image_classification.colorectal_histology import ColorectalHistologyLarge
from tensorflow_datasets.image_classification.cycle_gan import CycleGAN
from tensorflow_datasets.image_classification.deep_weeds import DeepWeeds
from tensorflow_datasets.image_classification.diabetic_retinopathy_detection import DiabeticRetinopathyDetection
from tensorflow_datasets.image_classification.dmlab import Dmlab
from tensorflow_datasets.image_classification.domainnet import Domainnet
from tensorflow_datasets.image_classification.dtd import Dtd
from tensorflow_datasets.image_classification.eurosat import Eurosat
from tensorflow_datasets.image_classification.flowers import TFFlowers
from tensorflow_datasets.image_classification.food101 import Food101
from tensorflow_datasets.image_classification.geirhos_conflict_stimuli import GeirhosConflictStimuli
from tensorflow_datasets.image_classification.horses_or_humans import HorsesOrHumans
from tensorflow_datasets.image_classification.i_naturalist2018 import INaturalist2018
from tensorflow_datasets.image_classification.imagenet import Imagenet2012
from tensorflow_datasets.image_classification.imagenet2012_corrupted import Imagenet2012Corrupted
from tensorflow_datasets.image_classification.imagenet2012_multilabel import Imagenet2012Multilabel
from tensorflow_datasets.image_classification.imagenet2012_real import Imagenet2012Real
from tensorflow_datasets.image_classification.imagenet2012_subset import Imagenet2012Subset
from tensorflow_datasets.image_classification.imagenet_a import ImagenetA
from tensorflow_datasets.image_classification.imagenet_lt import ImagenetLt
from tensorflow_datasets.image_classification.imagenet_r import ImagenetR
from tensorflow_datasets.image_classification.imagenet_resized import ImagenetResized
from tensorflow_datasets.image_classification.imagenet_sketch import ImagenetSketch
from tensorflow_datasets.image_classification.imagenet_v2 import ImagenetV2
from tensorflow_datasets.image_classification.imagenette import Imagenette
from tensorflow_datasets.image_classification.imagewang import Imagewang
from tensorflow_datasets.image_classification.inaturalist import INaturalist2017
from tensorflow_datasets.image_classification.lfw import LFW
from tensorflow_datasets.image_classification.malaria import Malaria
from tensorflow_datasets.image_classification.mnist import EMNIST
from tensorflow_datasets.image_classification.mnist import FashionMNIST
from tensorflow_datasets.image_classification.mnist import KMNIST
from tensorflow_datasets.image_classification.mnist import MNIST
from tensorflow_datasets.image_classification.mnist_corrupted import MNISTCorrupted
from tensorflow_datasets.image_classification.omniglot import Omniglot
from tensorflow_datasets.image_classification.oxford_flowers102 import OxfordFlowers102
from tensorflow_datasets.image_classification.oxford_iiit_pet import OxfordIIITPet
from tensorflow_datasets.image_classification.patch_camelyon import PatchCamelyon
from tensorflow_datasets.image_classification.pet_finder import PetFinder
from tensorflow_datasets.image_classification.places365_small import Places365Small
from tensorflow_datasets.image_classification.plant_leaves import PlantLeaves
from tensorflow_datasets.image_classification.plant_village import PlantVillage
from tensorflow_datasets.image_classification.plantae_k import PlantaeK
from tensorflow_datasets.image_classification.quickdraw import QuickdrawBitmap
from tensorflow_datasets.image_classification.resisc45 import Resisc45
from tensorflow_datasets.image_classification.rock_paper_scissors import RockPaperScissors
from tensorflow_datasets.image_classification.siscore import Siscore
from tensorflow_datasets.image_classification.smallnorb import Smallnorb
from tensorflow_datasets.image_classification.so2sat import So2sat
from tensorflow_datasets.image_classification.stanford_dogs import StanfordDogs
from tensorflow_datasets.image_classification.stanford_online_products import StanfordOnlineProducts
from tensorflow_datasets.image_classification.stl10 import Stl10
from tensorflow_datasets.image_classification.sun import Sun397
from tensorflow_datasets.image_classification.svhn import SvhnCropped
from tensorflow_datasets.image_classification.uc_merced import UcMerced
from tensorflow_datasets.image_classification.visual_domain_decathlon import VisualDomainDecathlon
