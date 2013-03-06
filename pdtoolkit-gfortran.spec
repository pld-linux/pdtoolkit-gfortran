Summary:	Modified gfortran parser for use in PDToolkit
Summary(pl.UTF-8):	Zmodyfilowany parser gfortranu dla PDToolkitu
Name:		pdtoolkit-gfortran
Version:	4.0.2
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://www.cs.uoregon.edu/research/paracomp/pdtoolkit/Download/gfortran-pdt.tar.gz
# Source0-md5:	fa4f9083a152ce449cf60782b5b72093
URL:		http://www.cs.uoregon.edu/research/paracomp/pdtoolkit/
BuildRequires:	gmp-devel
BuildRequires:	mpfr-devel
Requires:	pdtoolkit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modified gfortran parser for use in PDToolkit.

%description -l pl.UTF-8
Zmodyfilowany parser gfortranu dla PDToolkitu.

%prep
%setup -q -n gcc-%{version}-pdt

%build
install -d obj-pdt
cd obj-pdt
CFLAGS="%{rpmcflags}" \
../configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libdir} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--enable-cmath \
	--enable-languages="c,f95" \
	--enable-long-long \
	--enable-threads=posix \
	--disable-multilib \
	--disable-nls \
	--with-demangler-in-ld \
	--with-system-zlib \
	--with-slibdir=%{_slibdir} \
	--without-x \
	%{_target_platform}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/pdtoolkit/bin/pdt_gfortran
install obj-pdt/gcc/{cc1,f951,gfortran} $RPM_BUILD_ROOT%{_libdir}/pdtoolkit/bin/pdt_gfortran

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pdtoolkit/bin/pdt_gfortran/cc1
%attr(755,root,root) %{_libdir}/pdtoolkit/bin/pdt_gfortran/f951
%attr(755,root,root) %{_libdir}/pdtoolkit/bin/pdt_gfortran/gfortran
